const kue = require('kue');

const obj = {
  phoneNumber: '',
  message: '',
}

const push_notification_code = kue.createQueue();

const job = push_notification_code.create('job', obj).save((err) => {
  if (err) {
    console.log('Notification job failed');
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
}).complete(() => console.log('Notification job completed'));
