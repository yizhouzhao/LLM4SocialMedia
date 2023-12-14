from sklearn.metrics import precision_score, recall_score, f1_score
labels = [1,1,1,1,1,1,1,1,1,1]

def evaluate(predictions, labels):
    precision = precision_score(labels, predictions)
    recall = recall_score(labels, predictions)
    f1 = f1_score(labels, predictions)

    return precision, recall, f1

def main():
    precision, recall, f1 = evaluate(predictions, labels)

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1}")

if __name__ == "__main__":
    main()