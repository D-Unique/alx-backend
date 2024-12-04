import kue from 'kue';

const jobs = kue.createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to emmanuel ${phoneNumber}, with message: ${message}`);
}

jobs.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
