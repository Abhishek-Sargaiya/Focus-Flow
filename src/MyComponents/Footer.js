
import React from 'react'

export const Footer = () => {
    let footerStle = {
      position: "relative",
      bottom: "0",
      left: "0",
      width: "100%",
    }
  return (
    <footer className="bg-dark text-light py-3" style={footerStle}>
      <p className='text-center'>Copyright &copy; MyTodosList.com</p>
    </footer>
  )
}

export default Footer;