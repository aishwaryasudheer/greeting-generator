def find_runner_up_score(scores):
    unique_scores = list(set(scores))  # Remove duplicates
    unique_scores.sort(reverse=True)   # Sort scores in descending order
    if len(unique_scores) > 1:
        return unique_scores[1]  # Return the second highest score
    else:
        return None  # No runner-up score if there's only one unique score

def main():
    n = int(input("Please enter the number of participants: "))
    scores = list(map(int, input("Please enter the scores separated by spaces: ").split()))

    if len(scores) != n:
        print("Error: Number of provided scores doesn't match the number of participants.")
        return

    runner_up_score = find_runner_up_score(scores)
    if runner_up_score is not None:
        print(runner_up_score)
    else:
        print("Error: Unable to find a runner-up score.")

if __name__ == "__main__":
    main()
