import os
LIST = 'catatan.txt'

def load_todo():
	todo = []
	if os.path.exists(LIST):
		with open(LIST, 'r', encoding='utf-8') as f:
			for line in f:
				line = line.strip()
				if line:
					status = 'done' if line.startswith('[x]') else 'pending'
					task = line[4:]
					todo.append({'task': task, 'status': status})
	return todo

def save_todo(todo):
	with open(LIST, 'w', encoding='utf-8') as f:
		for todo in todo:
			status = '[x]' if todo['status'] == 'done' else '[ ]'
			f.write(f"{status} {todo['task']}\n")

def pause_and_clear():
	input("Tekan Enter untuk melanjutkan...")
	os.system('cls')

def show_todo(todo, filter_by=None):
	os.system('cls')
	print("="*50)
	print("\n\t Kelompok 3 To Do List\t\n")
	print("="*50)
	if not todo:
		print("Belum ada to-do.")
		pause_and_clear()
		return
	for i, todo in enumerate(todo, 1):
		if filter_by and todo['status'] != filter_by:
			continue
		status = '✓' if todo['status'] == 'done' else ' '
		print(f"{i}. [{status}] {todo['task']}")
	pause_and_clear()

def add_todo(todo):
	os.system('cls')
	task = input("Masukkan to-do baru: ").strip()
	if task:
		todo.append({'task': task, 'status': 'pending'})
		save_todo(todo)
		print("To-do berhasil ditambahkan!")
	pause_and_clear()

def edit_todo(todo):
	os.system('cls')
	show_todo(todo)
	i_input = input("Pilih nomor to-do yang ingin diedit: ").strip()
	if not i_input.isdigit():
		print("Input tidak valid.")
		pause_and_clear()
		return
	i = int(i_input) - 1
	if 0 <= i < len(todo):
		new_task = input("Masukkan to-do baru: ").strip()
		if new_task:
			todo[i]['task'] = new_task
			save_todo(todo)
			print("To-do berhasil diedit!")
	else:
		print("Nomor tidak valid.")
	pause_and_clear()

def delete_todo(todo):
	show_todo(todo)
	i_input = input("Pilih nomor to-do yang ingin dihapus: ").strip()
	if not i_input.isdigit():
		print("Input tidak valid.")
		pause_and_clear()
		return
	i = int(i_input) - 1
	if 0 <= i < len(todo):
		todo.pop(i)
		save_todo(todo)
		print("To-do berhasil dihapus!")
	else:
		print("Nomor tidak valid.")
	pause_and_clear()
		
def mark_done(todo):
	os.system('cls')
	show_todo(todo, filter_by='pending')
	i_input = input("Pilih nomor to-do yang ingin ditandai selesai: ").strip()
	if not i_input.isdigit():
		print("Input tidak valid.")
		pause_and_clear()
		return
	i = int(i_input) - 1
	if 0 <= i < len(todo) and todo[i]['status'] == 'pending':
		todo[i]['status'] = 'done'
		save_todo(todo)
		print("To-do berhasil ditandai selesai!")
	else:
		print("Nomor tidak valid atau sudah selesai.")
	pause_and_clear()
