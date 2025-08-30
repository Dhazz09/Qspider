# Negative Number Extractor

def extract_negatives(numbers):
    negatives = []
    for num in numbers:
        if num < 0:
            negatives.append(num)
    return negatives
sample_list = [10, -5, 0, -22, 7, -1, 3]
result = extract_negatives(sample_list)

print(f" Negative numbers: {result}")