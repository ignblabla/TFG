import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/Form.css";
import LoadingIndicator from "./LoadingIndicator";
import { FaUser, FaLock } from "react-icons/fa";
import logoEscudo from "../assets/escudo.png"; 

function Form({ route, method }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    
    const [menuOpen, setMenuOpen] = useState(false);
    
    const navigate = useNavigate();

    const isLogin = method === "login";
    const title = isLogin ? "Acceso de Hermanos" : "Registro de Hermano";

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        try {
            const res = await api.post(route, { username, password });
            if (isLogin) {
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
                navigate("/");
            } else {
                navigate("/login");
            }
        } catch (error) {
            alert("Error en la autenticación: " + error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="site-wrapper">
            <nav className="navbar">
                <div className="logo-container">
                    <img src={logoEscudo} alt="Escudo San Gonzalo" className="nav-logo" />
                    <div className="logo-text">
                        <h4>Hermandad de San Gonzalo</h4>
                        <span>SEVILLA</span>
                    </div>
                </div>

                <button className="menu-toggle" onClick={() => setMenuOpen(!menuOpen)}>
                    {menuOpen ? "✕" : "☰"}
                </button>

                <ul className={`nav-links ${menuOpen ? "active" : ""}`}>
                    <li><a href="#hermandad">Hermandad</a></li>
                    <li><a href="#titulares">Titulares</a></li>
                    <li><a href="#agenda">Agenda</a></li>
                    <li><a href="#lunes-santo">Lunes Santo</a></li>
                    <li><a href="#multimedia">Multimedia</a></li>
                    <div className="nav-buttons-mobile">
                        <button className="btn-outline">Acceso Hermano</button>
                        <button className="btn-purple">Hazte Hermano</button>
                    </div>
                </ul>

                <div className="nav-buttons-desktop">
                    <button className="btn-outline">Acceso Hermano</button>
                    <button className="btn-purple">Hazte Hermano</button>
                </div>
            </nav>

            <main className="content-wrapper">
                <div className="login-card">
                    <div className="card-header-icon">
                        <FaUser />
                    </div>

                    <h2 className="card-title">{title}</h2>
                    <p className="card-subtitle">
                        {isLogin 
                            ? "Bienvenido al portal del hermano. Por favor, identifícate." 
                            : "Completa los datos para darte de alta."}
                    </p>

                    <form onSubmit={handleSubmit}>
                        <div className="input-group">
                            <label htmlFor="username">Usuario</label>
                            <div className="input-wrapper">
                                <FaUser className="input-icon" />
                                <input
                                    id="username"
                                    type="text"
                                    value={username}
                                    onChange={(e) => setUsername(e.target.value)}
                                    placeholder="ej. hermano123"
                                    required
                                />
                            </div>
                        </div>

                        <div className="input-group">
                            <label htmlFor="password">Contraseña</label>
                            <div className="input-wrapper">
                                <FaLock className="input-icon" />
                                <input
                                    id="password"
                                    type="password"
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    placeholder="********"
                                    required
                                />
                            </div>
                        </div>

                        {isLogin && (
                            <div className="forgot-password">
                                <a href="#">¿Olvidaste tu contraseña?</a>
                            </div>
                        )}

                        {loading && <LoadingIndicator />}
                        
                        <button type="submit" className="btn-login" disabled={loading}>
                            {isLogin ? "Iniciar Sesión" : "Registrarse"}
                        </button>
                    </form>

                    <div className="card-footer">
                        <p>
                            {isLogin ? (
                                <>¿Aún no tienes cuenta? <a href="/register">Solicitar alta</a></>
                            ) : (
                                <>¿Ya tienes cuenta? <a href="/login">Inicia sesión aquí</a></>
                            )}
                        </p>
                    </div>
                </div>
            </main>
        </div>
    );
}

export default Form;