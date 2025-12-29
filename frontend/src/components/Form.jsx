import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/Form.css"
import LoadingIndicator from "./LoadingIndicator";
import { FaUser } from "react-icons/fa";
import { FaLock } from "react-icons/fa";

function Form({ route, method }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
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
                            <i className="fas fa-user">
                                <FaUser />
                            </i>
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
                            <i className="fas fa-lock">
                                <FaLock />
                            </i>
                            <input
                                id="password"
                                type="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                placeholder="........"
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
    );
}

export default Form