document.addEventListener('DOMContentLoaded', () => {
    //make 'enter' key submit msg
    let msg = document.querySelector('#user_message');
    msg.addEventListener('keyup', event => {
        if (event.keyCode === 13) {
            document.querySelector('#send_message').click();
        };
    });
})