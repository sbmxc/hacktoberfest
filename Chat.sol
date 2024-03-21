pragma solidity ^0.4.6;
import "remix_tests.sol"; // this import is automatically injected by Remix.

contract ChatApp {
   
   // event NewMessage(string message, address user, uint timestamp, string roomName);

    

    struct Message {
        string message;
        string userName;
        uint timestamp;
    }
    
   
    mapping(uint256 => Message[]) chats;
  
    
    function createNewChat(string _chatName) external view returns (uint) {
        uint256 chatId = uint256(sha256(abi.encode(now, _chatName)));
        Message[] chat; 
        chats[chatId] = chat;
        return chatId;
        
    }

  //  Send a message to a chat and fire an event to be caught by the UI
    function sendMessage(string _msg,  uint _chat, string _uname) external {
        Message memory message = Message(_msg, _uname, block.timestamp);
        chats[_chat].push(message);
      // NewMessage(_msg, msg.sender, block.timestamp, _roomName);
    }

  
 
    function getMessageCountForRoom(uint _chatId) external view returns (uint) {
        return chats[_chatId].length;
    }

    // There is no support for returning a struct to web3, so this needs to be
    // returned as multiple items. This will throw an error if the index is invalid
    function getMessageByIndexForChat(uint256 _chatId, uint _index) external view returns (string, string, uint) {
        Message memory message = chats[_chatId][_index];
        return (message.message, message.userName, message.timestamp);
    }


}