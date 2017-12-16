from sklearn import tree
training_data = [[170,9],[175,10],[180,8],[178,8],[182,7],[130,3],[120,4],[130,2],[138,5]]
training_labels = [1,1,1,1,1,0,0,0,0]
clf = tree.DecisionTreeClassifier()
#[145,6] 0
clf = clf.fit(training_data,training_labels)
print clf.predict([[145,6]])
