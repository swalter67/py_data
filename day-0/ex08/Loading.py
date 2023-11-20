import time
import shutil


def format_time(seconds):
    """
    Format the given time in seconds as MM:SS.

    Args:
        seconds (float): Time in seconds.

    Returns:
        str: Formatted time in the format MM:SS.
    """
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst: range) -> None:
    """
    Simulate a progress bar for iterating through a range.

    Args:
        lst (range): The range to iterate through.

    Yields:
        Any: The current item from the range.
        is a keyword in Python used in the context of creating generators.
        Generators are a way to create iterators, which are objects used to
        iterate over a sequence of values without having to store all those
        values in memory at once. Instead of generating allvalues and returning
        them in one go, a generator yields one value at a time whenever the
        yield statement is encountered.
    """
    # Get the total number of items in the range
    total = len(lst)
     # Record the start time for measuring elapsed time
    start_time = time.time()
    # Get the terminal width and calculate the progress bar width
    terminal_width = shutil.get_terminal_size().columns - 30
    progress_bar_width = terminal_width - 10

    for i, item in enumerate(lst, start=1):
        progress = int(i / total * progress_bar_width)

        
        # Calculate elapsed time, speed, and estimated time of arrival (ETA)
        elapsed_time = time.time() - start_time
        speed = i / elapsed_time
        eta = (total - i) / speed
        # Format elapsed time and ETA
        elapsed_formatted = format_time(elapsed_time)
        eta_formatted = format_time(eta)
        # Build the progress bar string
        progress_bar = f"|{'█' * progress:<{progress_bar_width}}|"
        # Calculate and format progress percentage
        progress_percentage = progress * 100 // progress_bar_width
        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
        # Build and format time-related information
        time_info = f"[{elapsed_formatted}<{eta_formatted}, {speed:.2f}it/s]"
        # Print the progress information, updating it in-place

        print(f"\r{progress_info} {time_info}", end="", flush=True)

        # Yield the current item from the range
        yield item


def main():
    for _ in ft_tqdm(range(0, 333)):
        pass


if __name__ == "__main__":
    main()