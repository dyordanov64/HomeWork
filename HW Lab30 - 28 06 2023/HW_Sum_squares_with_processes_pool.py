from time import sleep, time
import multiprocessing



# pr_name =  multiprocessing.current_process().name
# print(f'{pr_name} starts')

def calc_sum_squares(start, end, q):
	
	pr_name =  multiprocessing.current_process().name
	print(f'*********** {pr_name} is calculating sum of {start} to {end}')
	total_sum = q.get()
	# print(f'---- total_sum in {pr_name} = {total_sum}')

	# CPU bound
    
	total_sum += sum( map(lambda x:x**2, range(start, end)) )

	print(f'---- total_sum in {pr_name} = {total_sum}')
	q.put(total_sum)

def sequential(n,queue):
	calc_sum_squares(1, n//2, queue)
	calc_sum_squares(n//2, n+1, queue)

	# print(f'total_sum in sequential: {total_sum}')

def process_demo(max_number,queue):
	process_pool = []
	process_count = 2

	# for i in range(process_count):
	# 	# TODO : make it work !!!
	# 	start = i+1
	# 	end = max_number//process_count
	# 	print(f'{end}')

	# 	pr = multiprocessing.Process(target=calc_sum_squares, args=(start, end), kwargs={}, daemon=None)

	pr1= multiprocessing.Process(target=calc_sum_squares, name='pr1', args=(1, max_number//2,queue))
	pr2= multiprocessing.Process(target=calc_sum_squares, name='pr2', args=(max_number//2, max_number+1,queue))

	pr1.start();
	pr2.start();

	pr1.join()
	# print(f'pr1 finished [total_sum={total_sum}]')
	pr2.join()
	# print(f'pr2 finished [total_sum={total_sum}]')

	# print(f'total_sum in process_demo: {total_sum}')


if __name__ == "__main__":
	queue = multiprocessing.Queue()
	queue.put(0)
	max_number = 50_000_000

	start = time()
	# process_demo(max_number, queue)
	sequential(max_number, queue)
	end = time()
	print(f'Time: {end-start}')