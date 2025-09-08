Custom Metrics - Classification
====

Sparkflows already provides default model metrics. In addition, users can include custom metrics depending on their use case.
  
Load the label, prediction, and probability data in a separate workflow and use a SQL Node\Spark\PySpark node to compute Precision, Recall, F1 score, Rank Ordering, KS-Statistics, and Lift. 

End-to-End Example link: https://docs.sparkflows.io/en/latest/tutorials/end-to-end/index.html

**1. Read the Scoring Data**

  * label (true target)
  * prediction (predicted class)
  * probability (vector with class probabilities)

 .. figure:: ../_assets/tutorials/machine-learning/custom-metrics/prediction-data.png
   :alt: Custom Metrics
   :width: 70%

**2. Extract Probability of Positive Class With SplitProbabilityColumn Node**

  .. figure:: ../_assets/tutorials/machine-learning/custom-metrics/split-probability-column-node.png
     :alt: Custom Metrics
     :width: 70%

**3. Custom Metrics**

**By default, train/validation/test metrics** like accuracy,f1, AUC, rmse, etc provide. With the below custom metrics such as Rank Ordering / Deciles, KS Statistic and Lift:

 .. figure:: ../_assets/tutorials/machine-learning/custom-metrics/custom-metrics-code.png
   :alt: Custom Metrics
   :width: 70%

::

    import fire.util.mlmodel.SparkTrainMetrics
    import org.apache.spark.sql.{Row, SparkSession}
    import org.apache.spark.sql.functions.col
    import spark.implicits._
    import fire.output.OutputConfusionMatrixChart
    import org.apache.spark.sql.expressions.Window

    val labelCol = "churned_flag"
    val predictionCol = "prediction"
    val cmChartTitle  = "cmChartTitle"
    val confusionMatrixPredictedLabelLegend = "confusionMatrixPredictedLabelLegend"
    val confusionMatrixTargetLegend = "confusionMatrixTargetLegend"
    val confusionMatrixCountLegend = "confusionMatrixCountLegend"
    val cmChartDescription = "cmChartDescription"

    val tempDF = inDF.select(col(labelCol).cast("double").as(labelCol), col(predictionCol).cast("double").as(predictionCol),
                          col("prob1").as("prob1"))
    
    val outDF = tempDF.groupBy(labelCol, predictionCol).count()
    val convertedRows = outDF.collect()
    
    jobContext.workflowctx().confusionMatrix(node, convertedRows, confusionMatrixTargetLegend, confusionMatrixPredictedLabelLegend,
                                             confusionMatrixCountLegend);
    
    val cmGraphObj:OutputConfusionMatrixChart = SparkTrainMetrics.generateAndOutputConfusionMatrixChart(convertedRows, cmChartTitle, confusionMatrixPredictedLabelLegend,
          confusionMatrixTargetLegend, cmChartDescription)
    jobContext.workflowctx().outGraph(node, cmGraphObj)
    
    
    import org.apache.spark.sql.functions._
    
    val tp = tempDF.filter(col(predictionCol) === 1.0 && col(labelCol) === 1.0).count()
    val tn = tempDF.filter(col(predictionCol) === 0.0 && col(labelCol) === 0.0).count()
    val fp = tempDF.filter(col(predictionCol) === 1.0 && col(labelCol) === 0.0).count()
    val fn = tempDF.filter(col(predictionCol) === 0.0 && col(labelCol) === 1.0).count()
    
    val precision = if (tp + fp > 0) tp.toDouble / (tp + fp) else 0.0
    val recall    = if (tp + fn > 0) tp.toDouble / (tp + fn) else 0.0
    val f1        = if (precision + recall > 0) 2 * (precision * recall) / (precision + recall) else 0.0
    
    
    // Overall positive rate
    val totalPos = tempDF.filter(col(predictionCol) === 1.0).count().toDouble
    val totalCount = tempDF.count().toDouble
    val overallRate = totalPos / totalCount
    
    // Rank ordering into deciles
    val window = Window.orderBy(col("prob1").desc)
    val ranked = tempDF.withColumn("row_num", row_number().over(window))
      .withColumn("decile", ceil(col("row_num") / (totalCount / 10)))
    
    // Aggregate by decile
    val decileAgg = ranked.groupBy("decile")
      .agg(
        count("*").alias("count"),
        sum(when(col(predictionCol) === 1.0, 1).otherwise(0)).alias("positives")
      )
      .withColumn("positive_rate", col("positives") / col("count"))
      .withColumn("lift", col("positive_rate") / lit(overallRate))
      .orderBy(desc("decile"))
    
    
    jobContext.workflowctx().printDataFrame(node, decileAgg.collect(), decileAgg.schema)
    
    // ---- KS-Statistic ----
    val cumAgg = decileAgg
      .withColumn("cumPos", sum("positives").over(Window.orderBy(desc("decile"))))
      .withColumn("cumCount", sum("count").over(Window.orderBy(desc("decile"))))
      .withColumn("cumPosRate", col("cumPos") / lit(totalPos))
      .withColumn("cumNegRate", (col("cumCount") - col("cumPos")) / (lit(totalCount - totalPos)))
      .withColumn("ks", abs(col("cumPosRate") - col("cumNegRate")))
    
    val ksValue = cumAgg.agg(max("ks")).first().getDouble(0)
    
    val metrics = s"Precision=$precision \n Recall=$recall \n F1=$f1 \n KS-Statistic = $ksValue"
    jobContext.workflowctx().out(metrics)
    outDF.registerTempTable("temp_table")
    apps-fileview.texmex_20250828.00_p3
    code.txt
    Displaying code.txt.

**Output**

* Confusion Metrics

 .. figure:: ../_assets/tutorials/machine-learning/custom-metrics/output-confusion-metrics.png
   :alt: Custom Metrics
   :width: 70%

* Other Metrics

 .. figure:: ../_assets/tutorials/machine-learning/custom-metrics/output-other-metrics.png
   :alt: Custom Metrics
   :width: 70%























