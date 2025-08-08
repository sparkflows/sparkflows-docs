Access Tokens
=============

Access tokens are used to authenticate and authorize users for various operations within Fire Insights.

.. figure:: ../_assets/security/Access-Tokens.png
   :alt: security
   :width: 60%

Edit Token Description
----------------------

This permission allows a user to edit the description of an access token.

* Only the **``owner``** of the token or an **``admin user``** can perform this action.
* It enables better token identification by allowing token owners to update the description of their tokens.

.. figure:: ../_assets/security/delete1Token.png
   :alt: security
   :width: 60%

.. figure:: ../_assets/security/Description01.png
   :alt: security
   :width: 60%

Delete Token
------------

This permission enables a user to delete a specific token.

* A token can be deleted by its **``owner``** or by a user who has the **``token.deleteAllTokens``** permission.
* Users with the `deleteAllTokens` permission can delete tokens created by **any user**, not just their own.

.. figure:: ../_assets/security/delete1Token.png
   :alt: security
   :width: 60%

.. figure:: ../_assets/security/deleteAllPermission.png
   :alt: security
   :width: 60%


Delete Multiple Tokens
----------------------

This functionality allows users to delete **``multiple access tokens``** in a single action.

* Upon selection of multiple tokens, the user can delete them in bulk.
* If a user selects tokens that they are **not authorized** to delete, a summary will be displayed after the operation:
  
  - Number of tokens **successfully deleted**
  - Number of **failed deletions**
  - **Reasons** for failures (e.g., lack of permission)

.. figure:: ../_assets/security/Delete-Multiple-Description.png
   :alt: security
   :width: 60%

.. figure:: ../_assets/security/delete-description-multiple.png
   :alt: security
   :width: 60%

This ensures transparency and provides a clear audit of actions taken.
