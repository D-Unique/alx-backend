import kue from 'kue';
const jobs = kue.createQueue();

const blacklisted = [4153518780, 4153518781];

const sendNotification = (phoneNumber, message, job, done) => {
    job.progress(0, 100, job);
    if (blacklisted.includes(phoneNumber)) {
        done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    } else {
        job.progress(50, 100, job);
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
        done();
    }

}
jobs.process('push_notification_code_2', 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
