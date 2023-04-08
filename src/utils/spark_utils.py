





# create DataFrame as a temporary view
# train.createOrReplaceTempView('table')

# spark.sql("SELECT work_type, count(work_type) as work_type_count FROM table WHERE stroke == 1 GROUP BY work_type ORDER BY work_type_count DESC").show()

# spark.sql("SELECT gender, count(gender) as count_gender, count(gender)*100/sum(count(gender)) over() as percent FROM table GROUP BY gender").show()

# spark.sql("SELECT gender, count(gender), (COUNT(gender) * 100.0) /(SELECT count(gender) FROM table WHERE gender == 'Male') as percentage FROM table WHERE stroke = '1' and gender = 'Male' GROUP BY gender").show()

# spark.sql("SELECT gender, count(gender), (COUNT(gender) * 100.0) /(SELECT count(gender) FROM table WHERE gender == 'Female') as percentage FROM table WHERE stroke = '1' and gender = 'Female' GROUP BY gender").show()


# spark.sql("SELECT age, count(age) as age_count FROM table WHERE stroke == 1 GROUP BY age ORDER BY age_count DESC").show()

# train.filter((train['stroke'] == 1) & (train['age'] > '50')).count()

# # fill in missing values
# train_f = train.na.fill('No Info', subset=['smoking_status'])
# # fill in miss values with mean

# mean = train_f.select(mean(train_f['bmi'])).collect()
# mean_bmi = mean[0][0]
# train_f = train_f.na.fill(mean_bmi,['bmi'])


# assembler = VectorAssembler(inputCols=['genderVec',
#  'age',
#  'hypertension',
#  'heart_disease',
#  'ever_marriedVec',
#  'work_typeVec',
#  'Residence_typeVec',
#  'avg_glucose_level',
#  'bmi',
#  'smoking_statusVec'],outputCol='features')


# dtc = DecisionTreeClassifier(labelCol='stroke',featuresCol='features')


# pipeline = Pipeline(stages=[gender_indexer, ever_married_indexer, work_type_indexer, Residence_type_indexer,
#                            smoking_status_indexer, gender_encoder, ever_married_encoder, work_type_encoder,
#                            Residence_type_encoder, smoking_status_encoder, assembler, dtc])

# train_data,test_data = train_f.randomSplit([0.7,0.3])

# model = pipeline.fit(train_data)

# dtc_predictions = model.transform(test_data)


# # Select (prediction, true label) and compute test error
# acc_evaluator = MulticlassClassificationEvaluator(labelCol="stroke", predictionCol="prediction", metricName="accuracy")
# dtc_acc = acc_evaluator.evaluate(dtc_predictions)
# print('A Decision Tree algorithm had an accuracy of: {0:2.2f}%'.format(dtc_acc*100))
