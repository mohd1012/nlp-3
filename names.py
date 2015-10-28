#example from nlp in python book
#using naive bayes to classify gender of name
#still figuring out import statements lol
import nltk
from nltk.corpus import names
import random



def main():
	names_set = ([(name, 'male') for name in names.words('male.txt')] +
		[(name, 'female') for name in names.words('female.txt')])
	random.shuffle(names_set)
	feature_set = [(gender_features(n), g) for (n, g) in names_set]
	#train by the first half of the names and then use the second
	#half of names to check for errors in feature extractor
	train_set, test_set = feature_set[500:], feature_set[:500]
	classifier = nltk.NaiveBayesClassifier.train(train_set)

	#test
	print("========== Using Naive Bayes ==========\n===== to Classify Gender of Names =====")
	print
	print("\ntesting Neo") 
	print(classifier.classify(gender_features('Neo')))
	print("testing Trinity")
	print(classifier.classify(gender_features('Trinity')) + "\n")
	classifier.show_most_informative_features(5)

	print("\nAccuracy of Training on Test Set: " + str(nltk.classify.accuracy(classifier, test_set)))
	devtest_names = names_set[500:1500]
	devtest_set = [(gender_features(n), g) for (n, g) in names_set]
	errors = []
	for (name, tag) in devtest_names:
		guess = classifier.classify(gender_features(name))
		if guess != tag:
			errors.append((tag, guess, name))
	print("\n==== Printing Some Errors ====")
	for (tag, guess, name) in errors[:10]:
		print("correct: " + tag + ", guess: " + guess + ", name: " + str(name))

	print("\n==== Using a Different Feature Extractor ====\n=============== For Suffixes ================")
	feature_set2 = [(updated_gender_features(n), g) for (n, g) in names_set]
	train_set2, test_set2 = feature_set2[500:], feature_set2[:500]
	classifier2 = nltk.NaiveBayesClassifier.train(train_set2)
	classifier2.show_most_informative_features(5)
	print("\nAccuracy of Training on Test Set: " + str(nltk.classify.accuracy(classifier2, test_set2)))

def gender_features(word):
	if len(word) != 1:
		return {'last_letter' : word[-1]}
	else:
		return {'last_letter' : '.'}

def updated_gender_features(word):
	return {'suffix1' : word[-1:], 'suffix2' : word[-2:]}

if __name__ == "__main__":
	main()