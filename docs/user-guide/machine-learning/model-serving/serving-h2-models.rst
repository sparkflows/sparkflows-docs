Serving H2O Models
==================

H2O allows you to persist the models you have built to either a Plain Old Java Object (POJO) or a Model Object, Optimized (MOJO).

Fire Insights has the following processors for persisting the H2O Models.

  * H2OMojoSave
  * H2OModelSave

Once the H2O model is saved, they can be used for scoring and serving.

H2O-generated MOJO and POJO models are intended to be easily embeddable in any Java environment. The only compilation and runtime dependency for a generated model is the h2o-genmodel.jar file produced as the build output of these packages.

H2OModelLoad or H2OMojoLoad Processors in Fire Insights can be used to make a batch predictions or real-time prediction using Spark Streaming. Or you can expose your model as a REST API.

https://h2o-release.s3.amazonaws.com/h2o/rel-ueno/2/docs-website/h2o-docs/pojo-quick-start.html


Serving H2O MOJO models
------------------------

The below page on the H2O website gives details on serving a MOJO model.

http://docs.h2o.ai/h2o/latest-stable/h2o-docs/productionizing.html#step-2-compile-and-run-the-mojo


Serving H2O POJO models
-----------------------

The details for serving a POJO models is described in this page.

http://docs.h2o.ai/h2o/latest-stable/h2o-docs/productionizing.html#building-a-pojo

.. code-block:: java
   :linenos:
   
   import java.io.*;
   import hex.genmodel.easy.RowData;
   import hex.genmodel.easy.EasyPredictModelWrapper;
   import hex.genmodel.easy.prediction.*;

   public class main {
    private static String modelClassName = "gbm_pojo_test";

    public static void main(String[] args) throws Exception {
      hex.genmodel.GenModel rawModel;
      rawModel = (hex.genmodel.GenModel) Class.forName(modelClassName).newInstance();
      EasyPredictModelWrapper model = new EasyPredictModelWrapper(rawModel);

      RowData row = new RowData();
      row.put("Year", "1987");
      row.put("Month", "10");
      row.put("DayofMonth", "14");
      row.put("DayOfWeek", "3");
      row.put("CRSDepTime", "730");
      row.put("UniqueCarrier", "PS");
      row.put("Origin", "SAN");
      row.put("Dest", "SFO");

      BinomialModelPrediction p = model.predictBinomial(row);
      System.out.println("Label (aka prediction) is flight departure delayed: " + p.label);
      System.out.print("Class probabilities: ");
      for (int i = 0; i < p.classProbabilities.length; i++) {
        if (i > 0) {
          System.out.print(",");
        }
        System.out.print(p.classProbabilities[i]);
      }
      System.out.println("");
    }
   }



Useful links:

https://medium.com/spikelab/building-a-machine-learning-application-using-h2o-ai-67ce3681df9c



