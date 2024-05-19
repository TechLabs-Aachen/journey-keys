"use client"
import { useEffect, useRef, useState, useCallback } from 'react'
import { useInterval } from '../hook'
import styles from '../page.module.css'

const me = "Jian Yang CEO"

function ChatMessage(props) {
  const { senderName, message } = props

  return (
    <div
      className={styles.chatbox}
      style={{ alignSelf: senderName === me ? "self-end" : "self-start" }}>
      <p className={styles.chatmsg}>{message}</p>
      <p
        className={styles.chatsender}
        style={{ textAlign: senderName === me ? "right" : "left" }}
      >{senderName}</p>
    </div>
  )
}

export default function Home() {

  const chatboxRef = useRef(null);
  const [inputMessage, setInputMessage] = useState('')
  const [messages, setMessages] = useState([])

  const sendMsgCb = useCallback((msg) => {
    fetch('/api/send', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ message: msg, senderName: me })
    })
      .then(res => res.json())
      .then(data => { console.log(data); setMessages([...messages, data]) })

  }, [inputMessage, messages])

  useEffect(() => {
    if (!chatboxRef) return
    chatboxRef.current.scrollTo(0, chatboxRef.current.scrollHeight);
  }, [chatboxRef, messages])

  useEffect(() => {
    fetch('/api/log').then(res => res.json()).then(data => setMessages(data))
  }, [])

  useInterval(() => {
    fetch('/api/newmsg?id='+me)
      .then(res => res.json())
      .then(data => {
        if (data.msg.length > 0){ 
          console.log("query new msg", data.msg)
          setMessages(m => [...m, ...data.msg])
        }
      })
  }, 1500)

  return (
    <main className={styles.main}>
      <h1>Aviato Customer Service (admin)✈️</h1>
      <div ref={chatboxRef} className={styles.chat} >
        <ChatMessage
          senderName="Jian Yang CEO"
          message="Hello, Erlich Bachman is dead. He give me, good friend, company Aviato." />
        {messages.map((msg, i) => <ChatMessage key={i} {...msg} />)}
      </div>
      <div className={styles.chatform}>
        <input
          className={styles.chatinput}
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          type="text"
          placeholder='Enter your message'
          autoComplete='off' />
        <button
          className={styles.chatbutton}
          onClick={() => { sendMsgCb(inputMessage); setInputMessage('') }}
        >✈️</button>
      </div>
    </main>
  )
}
