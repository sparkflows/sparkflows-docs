Serving H2O Models
==================

Fire Insights has the following processors for persisting the H2O Models.

- H2OMojoSave
- H2OPojoSave

Once the H2O model is saved, they can be used for serving.

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






