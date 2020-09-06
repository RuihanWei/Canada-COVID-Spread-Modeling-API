import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import Chart from './components/Chart';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';
import Select from 'react-select';


function App() {
  const[case_, setcase_] = useState("25");
  const[province, setprovince] = useState("Ontario");
  const[country, setcountry] = useState("Canada");

  const [dates, setdates] = useState([]);
  const [values, setvalues] = useState([]);
  const [availableCases, setavailableCases] = useState([]);
  const [availableProvinces, setavailableProvinces] = useState([]);

  useEffect(() => {
      fetch(`/getForecast/${case_}/${country}/${province}`).then(res => res.json()).then(data => {
        setdates(data.dates);
        setvalues(data.values);
      });
      
  }, []);
  
  useEffect(() => {
    fetch(`/getCases/${country}/${province}`).then(res => res.json()).then(data => {
      setavailableCases(data.cases);
    });
  }, []);

  useEffect(() => {
    fetch('/getProvinces').then(res => res.json()).then(data => {
      setavailableProvinces(data.provinces);
    });
  }, []);

  const onSelectMobility = (event) => {
      fetch(`/getForecast/${event.value}/${country}/${province}`).then(res => res.json()).then(data => {
        setdates(data.dates);
        setvalues(data.values);
      });

    console.log('case changed');
    setcase_(event.value);
  }

  const onSelectProvince = (event) => {
    fetch(`/getCases/${case_}/${country}/${province}`).then(res => res.json()).then(data => {
      setavailableCases(data.cases);
    });
    console.log('Cases changed');
    setprovince(event.value);
  }

  var title = `case: ${case_}, country: ${country}, province: ${province}`
  
  let chartData = {
    labels: dates,
    datasets:[
      {
        label:'Prediction',
        data: values
      }
    ]
  }

  var op = ["e", "r"]

  return (
    <div className="App">
      <Dropdown options={availableProvinces} onChange={onSelectProvince} value = {province} placeholder="Select a Province" />
      <Dropdown options={availableCases} onChange={onSelectMobility} value = {country} placeholder="Select a mobility (percentage w.r.t. baseline)" />
      <Chart chartData = {chartData} displayTitle={title} />
    </div>
  );
}

export default App;
