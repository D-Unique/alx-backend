export default function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }
    for (let job in jobs) {
        const newqueue = queue.create('push_notification_code_3', job).save((err) => {
            if (!err) {
                console.log(`Notification job created: ${newqueue.id}`);
            }
        });
        newqueue.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        })
        newqueue.on('failed', (err) => {
            console.log(`Notification job ${job.id} failed: ${err}`)
        })
        newqueue.progress('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`)
        })
    }


}
