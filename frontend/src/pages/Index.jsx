import { Link } from "react-router-dom";
import "../styles/Index.css"
import logoEscudo from '../assets/escudo.png';

function Index() {
    return (
        <div className="site-wrapper">
            <nav>
                <div className="logo-container">
                    <img src={logoEscudo} alt="Escudo San Gonzalo" className="nav-logo" />
                    <div className="logo-text">
                        <h4>Hermandad de San Gonzalo</h4>
                        <span>SEVILLA</span>
                    </div>
                </div>
                <ul className="nav-links">
                    <li><a href="#hermandad">Hermandad</a></li>
                    <li><a href="#titulares">Titulares</a></li>
                    <li><a href="#agenda">Agenda</a></li>
                    <li><a href="#lunes-santo">Lunes Santo</a></li>
                    <li><a href="#multimedia">Multimedia</a></li>
                </ul>
                <div className="nav-buttons">
                    <button className="btn-outline">Acceso Hermano</button>
                    <button className="btn-purple">Hazte Hermano</button>
                </div>
            </nav>
        </div>
    );
}
export default Index;