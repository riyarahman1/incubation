import React, { useEffect, useState, useContext } from 'react'
import Header from '../components/Header'
import AuthContext from '../context/AuthContext'
import { useNavigate } from 'react-router-dom'


function HomePage() {
  const [notes, setNotes] = useState([])
  let { authTokens, logoutUser, user } = useContext(AuthContext)
  const Navigate = useNavigate()
  return (
    <div>

      <Header />
      <div className='container'>
        <div className='row mt-3 mb-3 justify-content-center'>
          <div className='col-md-3 px-3'>
            <button type="button" className="btn btn-primary btn-sm mt-2 mx-5" onClick={() => Navigate('/application')}>APPLICATION FORM</button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default HomePage