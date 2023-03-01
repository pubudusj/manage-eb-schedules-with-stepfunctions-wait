from datetime import datetime, timedelta


def lambda_handler(event, context):
    return calculate_wait_time(event)


def calculate_wait_time(event):
    payload = event['Payload']

    extra_wait_time = int(payload['flexibleTimeWindow']) + 1

    datetime_object = datetime.strptime(
        event['Payload']['scheduleDate'] + ' ' + event['Payload']['scheduleTime'] + ' +0000',
        '%Y-%m-%d %H:%M:%S %z'
    )

    result = datetime_object + timedelta(minutes=extra_wait_time)

    return {
        "waitUntil": result.astimezone().isoformat()
    }
