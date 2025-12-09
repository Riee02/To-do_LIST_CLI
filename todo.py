import os
import funct as ft

LIST = 'catatan.txt'

def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	while True:
		todo = ft.load_todo()
		print("\nMenu:")
		print("1. Tampilkan semua to-do")
		print("2. Tambah to-do")
		print("3. Edit to-do")
		print("4. Hapus to-do")
		print("5. Tandai selesai (mark done)")
		print("6. To-do tersisa")
		print("7. To-do selesai")
		print("0. Keluar")
		choice = input("Pilih menu: ").strip()
		if choice == '1':
			ft.show_todo(todo)
		elif choice == '2':
			ft.add_todo(todo)
		elif choice == '3':
			ft.edit_todo(todo)
		elif choice == '4':
			ft.delete_todo(todo)
		elif choice == '5':
			ft.mark_done(todo)
		elif choice == '6':
			ft.show_todo(todo, filter_by='pending')
		elif choice == '7':
			ft.show_todo(todo, filter_by='done')
		elif choice == '0':
			print("Keluar dari program")
			break
		else:
			print("Pilihan tidak valid.")
			ft.pause_and_clear()
    
if __name__ == "__main__":
	main()