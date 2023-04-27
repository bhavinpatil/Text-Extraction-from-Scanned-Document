# Text Extraction from Scanned Document
 Using Amazon Web Services Textract extracting handwritten and other formated text from Scanned Documents and Files

  Follow the steps to run the project

         pip install boto3
  Login to AWS console root account.
  
  Create an IAM user and select the AWS credential type as `Access Key - Programmatic access`
  
  Set permissions for `Attach existing policies directly` and click on `AdministratorAccess`
 
  Your IAM user will be created
  
  Go to `IAM > Users > USER_NAME` and create access key to use the AWS services
  
  Download the csv file of generated Access key ID and Secret access key
  
        pip install awscli
        aws configure --profile USER_NAME
        streamlit run python_web_application.py
        
   Now just enter your AWS access key and Secret Access Key for IAM user you have created and press enter and fill the Information as required with your project
   
   In `C:Users>USERNAME` a `.aws` folder will be created in which you will find config and creadentials files, you can change the information in it as you need
