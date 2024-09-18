document.addEventListener('DOMContentLoaded', function() 
//makes sure java script is executed after HTML document is fully executed and parsed.
{
    const chatInput = document.querySelector(".chat-input textarea"); // textarea where messages are entered
    const sendBtn = document.getElementById("send-btn"); //span containing send button
    const chatbox = document.querySelector(".chatbox"); //the whole chatbox
    const chatbotToggler = document.querySelector(".chatbot-toggler");  //toggler that controls visibility of chatbot
    const chatbotCloseIcon = document.querySelector('.Chatbot header span'); //header of chatbot: NEXUS AI and close button

    // Toggle chatbot visibility
    chatbotToggler.addEventListener('click', function() 
    {
        document.body.classList.toggle('show-Chatbot'); //on clicking the chatbot becomes visible
    });

    // Close button for chatbot
    chatbotCloseIcon.addEventListener('click', function() 
    {
        document.body.classList.remove('show-Chatbot'); // on clicking the chatbot is closed
    });

    // API Key and setup
    const API_KEY = "sk-proj-IJew4ed7RTjg4WJ8xHO2T3BlbkFJqxXRrltngsZmUhuRXjrn";
    const API_URL = "https://api.openai.com/v1/chat/completions"; //OpenAi API link to access
    //there seems to be some runtime error with API key since the requests are not going through

    // Function to create chat bubbles
    const createChatBubble = (message, className) => {
        const li = document.createElement("li");
        li.classList.add("chat", className); //creates list element and gets its className
        li.innerHTML = `<span class="material-symbols-outlined">${className === 'incoming' ? 'smart_toy' : ''}</span><p>${message}</p>`; //rewrites inner html content based off of incoming or outgoing class
        return li;
    };

    // Function to handle sending and receiving messages
    const handleChat = async () => {
        const userMessage = chatInput.value.trim(); //gets the message entered
        if (!userMessage) return;
        // if it is invalid it returns
        chatInput.value = ""; // Clear input after sending
        chatbox.appendChild(createChatBubble(userMessage, "outgoing")); // Show user message by including content into list item
        const incomingChatBubble = createChatBubble("Let me think...", "incoming");//placeholder until response is loaded
        chatbox.appendChild(incomingChatBubble); // Show placeholder message

        try //exceptiond handling in case response is not found or loaded
        {
            const response = await fetch(API_URL, { //using fetch function we are making a network request and await is used to wait for the fetch function to return some value
                method: "POST",
                headers: 
                {
                    "Content-Type": "application/json", //application is in JSON format
                    "Authorization": `Bearer ${API_KEY}` 
                },
                body: JSON.stringify({ //converts into string 
                    model: "gpt-3.5-turbo", //gpt model
                    messages: [{ role: "user", content: userMessage }]
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`); //throws an exception
            }

            const data = await response.json(); //waits for response 
            incomingChatBubble.querySelector('p').textContent = data.choices[0].message.content; // Display AI response
        } catch (error) 
        {
            console.error('Request failed', error);
            incomingChatBubble.querySelector('p').textContent = "Sorry, I can't connect to the brain right now. Try again later!";
        }
    };

    // Send message on button click
    sendBtn.addEventListener('click', handleChat);

    // Also allow Enter to send message
    chatInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            handleChat();
        }
    });
});