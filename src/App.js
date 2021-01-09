import React, { useState } from 'react';
import Clock from 'react-live-clock';
import 'moment-timezone';
import './App.css';
var x;

function App() {
  const [currentPath, setCurrentPath] = useState(0);
  const [startingCommunity, setStartingCommunity] = useState(0);
  const [destinationCommunity, setDestinationCommunity] = useState(0);
  const [popDests, setPopDests] = useState('');
  const [greetMessage, setGreetMessage] = useState('Chica-go-Flow is an app that finds the safest path between any 2 of the 77 community areas in the city of Chicago,moving through neighbouring communities, using a shortest-path algorithmic implmentation on crime-frequency analysis done on each community from 2001 to present day.');
  const [title, setTitle] = useState("Chica-go-Flow: An App to Move Around Chicago Safely");
  const [showButton, setShowButton] = useState(true);
  const [destinationMessage, setDestinationMessage] = useState('');
  const [thirdState, setThirdState] = useState(false);
  const [wrongNumber,setWrongNumber] = useState(true);
  var targetvalue;


  const returnedPath = e => {
    fetch('/returnedPath').then(res => res.json()).then(data => {
      setCurrentPath(data.returnedPath);
      setWrongNumber(false);
      setThirdState(true);
    });
    }

  const findPath = e => {
    e.preventDefault();
    if(1<=startingCommunity && 1<=destinationCommunity && destinationCommunity<=77 && startingCommunity<=77){
      fetch('/find',{
        method : 'POST',
        headers: {
          'Content-Type':'application/json'
        },
        body: JSON.stringify({
          startingCommunity : startingCommunity,
          destinationCommunity : destinationCommunity
        })
      })
      .then(response => response.json());
      returnedPath();
    }
  };

  function findPath2(){
      fetch('/find',{
        method : 'POST',
        headers: {
          'Content-Type':'application/json'
        },
        body: JSON.stringify({
          startingCommunity : startingCommunity,
          destinationCommunity : x
        })
      })
      .then(response => response.json());
      returnedPath();
  }

  const popDestinationReciever = e =>{
    fetch('/popDestReciever').then(res => res.json()).then(data => {
      let b = data.popDestReciever;
      var c = JSON.parse(b);
      setPopDests(c);
    });
  }

  const popularDestination = e => {
    fetch('/popDestGetter',{
      method : 'POST',
      headers: {
        'Content-Type':'application/json'
      },
      body: JSON.stringify({
        targetvalue : targetvalue
      })
    })
    .then(response => response.json());
    popDestinationReciever();
  }

  const handleStartingCommunityChange = (e) => {
    if(e.target.value>=1 && e.target.value<=77){setWrongNumber(false);}
    if(e.target.value>=1 && e.target.value<=77 && destinationCommunity>=1 && destinationCommunity<=77){setDestinationMessage("The most popular destinations from your source: ");}else{setDestinationMessage("");setWrongNumber(true);}
    setStartingCommunity(e.target.value);
    targetvalue = e.target.value;
    popularDestination();
  }

  const handleDestinationCommunityChange = (e) => {
    if(e.target.value>=1 && e.target.value<=77 && startingCommunity>=1 && startingCommunity<=77){setWrongNumber(false);}else{setWrongNumber(true);}
    setDestinationCommunity(e.target.value);
  }

  const hDCC2 = (e) => {
    x = popDests[0];
    findPath2();
  }

  const hDCC3 = (e) => {
    x = popDests[1];
    findPath2();
  }

  const hDCC4 = (e) => {
    x = popDests[2];
    findPath2();
  }

  const hDCC5 = (e) => {
    x = popDests[3];
    findPath2();
  }

  const hDCC6 = (e) => {
    x = popDests[4];
    findPath2();
  }

  const hDCC7 = (e) => {
    setDestinationCommunity(popDests[5]);
    x = popDests[5];
    findPath2();
  }

  const hDCC8 = (e) => {
    x = popDests[6];
    findPath2();
  }

  const hDCC9 = (e) => {
    x = popDests[7];
    findPath2();
  }

  const hDCC10 = (e) => {
    x = popDests[8];
    findPath2();
  }

  const hDCC11 = (e) => {
    x = popDests[9];
    findPath2();
  }


  const changeTitle = (e) => {
    setTitle('');
    setGreetMessage('');
    setShowButton(false);
  }

  const handleReturnHome = (e) => {
    setTitle("Chica-go-Flow: An App to Move Around Chicago Safely");
    setGreetMessage("Chica-go-Flow is an app that finds the safest path between any 2 of the 77 community areas in the city of Chicago,moving through neighbouring communities, using a shortest-path algorithmic implmentation on crime-frequency analysis done on each community from 2001 to present day.");
    setThirdState(false);
    setShowButton(true);
  }

  const handletoApp = (e) => {
    setThirdState(false);
  }

  return (
    <div className="App">
      <header className="App-header">
        <div className="title">{title}</div>
        <div>{greetMessage}</div>
        <p>Local Time in Chicago</p><Clock format={'HH:mm:ss'} ticking={true} timezone={'America/Chicago'} />
        <img src={"chicago.svg"} className="App-logo" alt="chicago.svg"/>
        {showButton ? <button className="button" onClick={changeTitle}>Continue to the App</button> : null }
        {!showButton && thirdState?<p>The safest path from your source to your destination, moving through neighbouring community areas is {currentPath}.</p> : null}
        {!showButton && thirdState?<span><button className="button" onClick ={handleReturnHome}>Return to App Intro</button><button className="button" onClick ={handletoApp}>Find Another Safest Path</button></span> : null}
        {!showButton && !thirdState? <form className="par">
        Starting Community:
        <br />
        <input
          type="number"
          pattern="[0-77]"
          name="startingCommunity"
          onInput={handleStartingCommunityChange}
          value={startingCommunity}
        />
        <br />
        Destination Community:
        <br />
        <input
          type="number"
          pattern="[0-77]"
          name="endingCommunity"
          value={destinationCommunity}
          onChange={handleDestinationCommunityChange}
        />
        <br />
            <button className="button" onClick={findPath}>Find The Safest Path</button>
        </form>: null}
        {!showButton && wrongNumber && !thirdState ? <p className="par"><small>Please Enter a Community Area Between 1 and 77 for Your Starting and Destination Point</small></p>:null}
        {!showButton && !thirdState ? <p className="par">{destinationMessage}</p> : null}
        {!showButton && !thirdState ? <span className="par"><button className="button" onClick ={hDCC2}>{popDests[0]}</button>
                                            <button className="button" onClick ={hDCC3}>{popDests[1]}</button>
                                            <button className="button" onClick ={hDCC4}>{popDests[2]}</button>
                                            <button className="button" onClick ={hDCC5}>{popDests[3]}</button>
                                            <button className="button" onClick ={hDCC6}>{popDests[4]}</button>
                                            <button className="button" onClick ={hDCC7}>{popDests[5]}</button>
                                            <button className="button" onClick ={hDCC8}>{popDests[6]}</button>
                                            <button className="button" onClick ={hDCC9}>{popDests[7]}</button>
                                            <button className="button" onClick ={hDCC10}>{popDests[8]}</button>
                                            <button className="button" onClick ={hDCC11}>{popDests[9]}</button>
                                        </span> : null}
      </header>
    </div>
  );
}



export default App;