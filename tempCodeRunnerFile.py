import os

LIST = 'catatan.txt'

def load_todos():
	todos = []
	if os.path.exists(LIST):
		with open(LIST, 'r', encoding='utf-8') as f:
			for line in f:
				line = line.strip()
				if line:
					status = 'done' if line.startswith('[x]') else 'pending'
					task = line[4:]
					todos.append({'task': task, 'status': status})
	return todos

def save_todos(todos):
	with open(LIST, 'w', encoding='utf-8') as f:
		for todo in todos:
			status = '[x]' if todo['status'] == 'done' else '[ ]'
			f.write(f"{status} {todo['task']}\n")

def pause_and_clear():
	input("Tekan Enter untuk melanjutkan...")
	os.system('cls' if os.name == 'nt' else 'clear')

def show_todos(todos, filter_by=None):
	os.system('cls' if os.name == 'nt' else 'clear')
	print("="*50)
	print("\t Kelompok 3 To Do List\t")
	print("="*50)
	if not todos:
		print("Belum ada to-do.")
		pause_and_clear()
		return
	for idx, todo in enumerate(todos, 1):
		if filter_by and todo['status'] != filter_by:
			continue
		status = '✓' if todo['status'] == 'done' else ' '
		print(f"{idx}. [{status}] {todo['task']}")
	pause_and_clear()

def add_todo(todos):
	os.system('cls' if os.name == 'nt' else 'clear')
	task = input("Masukkan to-do baru: ").strip()
	if task:
		todos.append({'task': task, 'status': 'pending'})
		save_todos(todos)
		print("To-do berhasil ditambahkan!")
	pause_and_clear()

def edit_todo(todos):
	os.system('cls' if os.name == 'nt' else 'clear')
	show_todos(todos)
	try:
		idx = int(input("Pilih nomor to-do yang ingin diedit: ")) - 1
		if 0 <= idx < len(todos):
			new_task = input("Masukkan to-do baru: ").strip()
			if new_task:
				todos[idx]['task'] = new_task
				save_todos(todos)
				print("To-do berhasil diedit!")
		else:
			print("Nomor tidak valid.")
	except ValueError:
		print("Input tidak valid.")
	pause_and_clear()

def delete_todo(todos):
	os.system('cls' if os.name == 'nt' else 'clear')
	show_todos(todos)
	try:
		idx = int(input("Pilih nomor to-do yang ingin dihapus: ")) - 1
		if 0 <= idx < len(todos):
			todos.pop(idx)
			save_todos(todos)
			print("To-do berhasil dihapus!")
		else:
			print("Nomor tidak valid.")
	except ValueError:
		print("Input tidak valid.")
	pause_and_clear()
		
def mark_done(todos):
	os.system('cls' if os.name == 'nt' else 'clear')
	show_todos(todos, filter_by='pending')
	try:
		idx = int(input("Pilih nomor to-do yang ingin ditandai selesai: ")) - 1
		if 0 <= idx < len(todos) and todos[idx]['status'] == 'pending':
			todos[idx]['status'] = 'done'
			save_todos(todos)
			print("To-do berhasil ditandai selesai!")
		else:
			print("Nomor tidak valid atau sudah selesai.")
	except ValueError:
		print("Input tidak valid.")
	pause_and_clear()

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	while True:
		todos = load_todos()
		print("\nMenu:")
		print("1. Tampilkan semua to-do")
		print("2. Tambah to-do")
		print("3. Edit to-do")
		print("4. Hapus to-do")
		print("5. Tandai selesai (mark done)")
		print("6. Tampilkan to-do yang belum selesai (remaining)")
		print("7. Tampilkan to-do yang sudah selesai (completed)")
		print("0. Keluar")
		choice = input("Pilih menu: ").strip()
		if choice == '1':
			show_todos(todos)
		elif choice == '2':
			add_todo(todos)
		elif choice == '3':
			edit_todo(todos)
		elif choice == '4':
			delete_todo(todos)
		elif choice == '5':
			mark_done(todos)
		elif choice == '6':
			show_todos(todos, filter_by='pending')
		elif choice == '7':
			show_todos(todos, filter_by='done')
		elif choice == '0':
			print("Terima kasih telah menggunakan To-Do List!")
			break
		else:
			print("Pilihan tidak valid.")
			pause_and_clear()
    
if __name__ == "__main__":
	main()
