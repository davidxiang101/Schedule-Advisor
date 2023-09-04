'use strict';

var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
const otherUserID = document.getElementById('other-user-id').textContent.trim();
const currentUserUsername = document
  .getElementById('current-username')
  .textContent.trim()
  .replace(/\"/g, '');

const webSocket = new WebSocket(
  `${window.location.protocol === 'https:' ? 'wss' : 'ws'}://${
    document.body.dataset.host
  }/wss/chat/${otherUserID}/`
);

console.log(
  `${window.location.protocol === 'https:' ? 'wss' : 'ws'}://${
    document.body.dataset.host
  }/wss/chat/${otherUserID}/`
);

webSocket.addEventListener('open', (event) => {
  //   document.getElementById(
  //     'message-wrapper'
  //   ).innerHTML += `<div class="alert alert-success alert-dismissible fade show" role="alert">
  //                Conversation has started.
  //               <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  //             </div>`;
});

webSocket.addEventListener('message', (event) => {
  const data = JSON.parse(event.data);
  console.log(data);
  const chatBody = document.getElementById('chat-body');
  let newMessage = '';

  if (data.senderUsername === currentUserUsername) {
    newMessage = `
    <li class="d-flex justify-content-end align-items-top mb-3">
    <div class="message card text-white align-items-top"  style= " background-color: #58bcf6bd;">
      <div class="card-body d-flex flex-column pt-1 pb-0">
        <p class=" sent fw-bold ">${data.message}</p>
        <p class="sent small"> </p>
      </div>
    </div>
    <span class="newmessagecircle circle d-flex align-self-center me-3"></span>   
    </li>
    `;
  } else {
    newMessage = `
    <li class="d-flex justify-content-start mb-4">
    <span class="newmessage2 circle d-flex align-self-center me-3"></span>
    <div class="message card text-white" style= "background-color: #aa91f4bd;">
      <div class="card-body d-flex flex-column pt-1 pb-0">
        <p class=" fw-bold">${data.message}</p>
        <p class="small fst-italic" ></p>
      </div>
    </div>
    </li>
    `;
  }
  chatBody.innerHTML += newMessage;
  console.log(`SenderUser: ${data.senderUsername}`);
  console.log(`currentUserUsername: ${currentUserUsername}`);
  console.log(data.senderUsername === currentUserUsername);
});

webSocket.addEventListener('error', (event) => {
  document.getElementById(
    'message-wrapper'
  ).innerHTML += `<div class="alert alert-danger alert-dismissible fade show" role="alert">
          An error occurred.
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>        
        </div>`;
});

webSocket.addEventListener('close', (event) => {
 // document.getElementById(
 //   'message-wrapper'
  //).innerHTML += `<div class="alert alert-warning alert-dismissible fade show" role="alert">
  //    Chat ended.
      
  //  </div>`;
});

document
  .getElementById('send-message-btn')
  .addEventListener('click', (event) => {
    event.preventDefault();
    console.log('Here');
    const messageInput = document.getElementById('message-body');
    webSocket.send(
      JSON.stringify({
        message: messageInput.value,
        senderUsername: currentUserUsername,
      })
    );
    messageInput.value = '';
  });

window.addEventListener('DOMContentLoaded', () => {
  setTimeout(function () {
    document.querySelectorAll('.alert').forEach((element) => {
      element.querySelectorAll('.btn-close').forEach((el) => {
        el.click();
      });
    });
  }, 2000);
});
