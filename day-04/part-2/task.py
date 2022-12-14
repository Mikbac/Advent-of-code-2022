# cat sample | python3 task.py
# cat input | python3 task.py

# Created by MikBac on 2022

def main():
	party_contains = 0
	while True:
		try:
			pair = input().strip()

			first_assignee_start = int(pair.split(',')[0].split('-')[0])
			first_assignee_end = int(pair.split(',')[0].split('-')[1])
			second_assignee_start = int(pair.split(',')[1].split('-')[0])
			second_assignee_end = int(pair.split(',')[1].split('-')[1])

			if (first_assignee_start <= second_assignee_start <= first_assignee_end) or (
					first_assignee_start <= second_assignee_end <= first_assignee_end) or (
					second_assignee_start <= first_assignee_start <= second_assignee_end) or (
					second_assignee_start <= first_assignee_end <= second_assignee_end):
				party_contains += 1
		except EOFError:
			break

	print('Answer: {}'.format(party_contains))


if __name__ == "__main__":
	main()
