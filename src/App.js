import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  const [username, setUsername] = useState("ajhd");
  const [password, setPassword] = useState("ajhd");

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  const handleLogin = e => {
    e.preventDefault();
    fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username,
        password: password
      })
    })
      .then(response => response.json())
  };

  return (
    <div className="App">
      <header className="App-header">

        ... no changes in this part ...

        <p>The current time is {currentTime}.</p>
      </header>
      <form>
          Username:
          <br />
          <input
            type="text"
            name="username"
            value={username}
          />
          <br />
          Password:
          <br />
          <input
            type="password"
            name="password"
            value={password}
          />
          <br />
          <button onClick={this.handleLogin()}>Login</button>
        </form>
    </div>
  );
}

/*class Login extends React.Component {
  state = {
    username: 'fjdh',
    password: 'dhihf'
  };
  
  
    handleLogin = e => {
      e.preventDefault();
      fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: this.state.username,
          password: this.state.password
        })
      })
        .then(response => response.json())
    };
  
  
    render() {
      return (
        <form onSubmit={this.handleSubmit}>
          Username:
          <br />
          <input
            type="text"
            name="username"
            value={this.state.username}
          />
          <br />
          Password:
          <br />
          <input
            type="password"
            name="password"
            value={this.state.password}
          />
          <br />
          <button onClick={this.handleLogin}>Login</button>
        </form>
      );
    }
  }*/

export default App;
//export default Login;