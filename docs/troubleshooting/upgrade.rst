Upgrade
=======

H2
--

H3
^^

Missing column: application_id in FIREDB.PUBLIC.ANALYSIS_FLOW_EXECUTION
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

After I upgrade to the latest Fire Release I get the error : Missing column: application_id in FIREDB.PUBLIC.ANALYSIS_FLOW_EXECUTION

After upgrading the Fire Server, it is important to upgrade the Database Schema.

* Upgrade it by running create-h2-db.sh or create-mysql-db.sh from the Fire install directory.
* This would upgrade your DB schema to the latest.

Otherwise you can run into an error like below, when you start the Fire Server::

  Exception in thread "main" org.springframework.beans.factory.BeanCreationException:
  Error creating bean with name 'entityManagerFactory' defined in class path resource   [org/springframework/boot/autoconfigure/orm/jpa/HibernateJpaAutoConfiguration.class]:
  Invocation of init method failed; nested exception is org.hibernate.HibernateException:

  Missing column: application_id in FIREDB.PUBLIC.ANALYSIS_FLOW_EXECUTION
