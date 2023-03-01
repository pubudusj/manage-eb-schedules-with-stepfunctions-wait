# Manage EventBridge One time schedules using StepFunctions Wait State

This project contains source code for a serverless application to create, and delete Amazon EventBridge one time schedules using Step Functions.
Here, Step Function execution will wait until the schedule triggers as per the flexibleTimeWindow.

## Blog Post

You may read more about this here: [Blog Post]

## Deploy the application

Below are the deployment details.
You need AWS CLI, SAM CLI and GIT installed in your machine.

1. Clone the repository: https://github.com/pubudusj/manage-eb-schedules-with-stepfunctions-wait
2. Go in to the directory `manage-eb-schedules-with-stepfunctions-wait`
3. Install dependencies with `sam build`
4. Deploy the stack with `sam deploy -g`

## Testing

1. Once the stack is deployed successfully, you can start a Step Functions execution with below payload format. All fields are required.
    ```
    {
      "scheduleDate": "YYYY-MM-DD",
      "scheduleTime": "hh:mm:ss",
      "flexibleTimeWindow": 5
    }
    ```
2. This will create a EventBridge schedule and until the schedule triggers, the Step function execution will wait and then delete the schedule after the flexibleTimeWindow.

## Cleanup

1. To delete the stack, use: `sam delete`
