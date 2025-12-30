import React from 'react';
import "../styles/AltaHermano.css"

const AltaHermano = () => {
    return (
        <main className="form-content">
            <div className="title-section">
                <h1 className="card-title">Alta de Hermano</h1>
                <p className="card-subtitle">Complete el formulario para solicitar su ingreso en la Hermandad.</p>
            </div>

            <div className="progress-container">
                <div className="progress-text">
                    <span className="step-label">Paso 1 de 4: Datos principales</span>
                    <span className="percentage">25%</span>
                </div>
                <div className="progress-bar-background">
                    <div className="progress-bar-fill" style={{ width: '25%'}}></div>
                </div>
            </div>

            <div className="card login-card-style">
                <div className="card-header">
                    <div className="card-header-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
                        </svg>
                    </div>
                    <h2 className="section-title">Datos personales</h2>
                </div>

                <div className="form-row">
                    <div className="input-group">
                        <label htmlFor="nombre">Nombre</label>
                        <div className="input-wrapper no-icon">
                            <input type="text" id="nombre" placeholder="Ej. Juan" />
                        </div>
                    </div>
                    <div className="input-group">
                        <label htmlFor="apellido1">Primer Apellido</label>
                        <div className="input-wrapper no-icon">
                            <input type="text" id="apellido1" placeholder="Ej. Pérez" />
                        </div>
                    </div>
                </div>

                <div className="form-row">
                    <div className="input-group">
                        <label htmlFor="apellido2">Segundo Apellido</label>
                        <div className="input-wrapper no-icon">
                            <input type="text" id="apellido2" placeholder="Ej. García" />
                        </div>
                    </div>
                    <div className="input-group">
                        <label htmlFor="dni">DNI / NIF</label>
                        <div className="input-wrapper">
                            <i className="input-icon-font">🪪</i>
                            <input type="text" id="dni" placeholder="12345678Z" />
                        </div>
                    </div>
                </div>

                <div className="form-row">
                    <div className="input-group">
                        <label htmlFor="nacimiento">Fecha de nacimiento</label>
                        <div className="input-wrapper no-icon">
                            <input type="date" id="nacimiento" />
                        </div>
                    </div>
                    <div className="input-group">
                        <label htmlFor="genero">Género</label>
                        <div className="input-wrapper no-icon">
                            <select id="genero" className="select-field">
                                <option value="">Seleccione una opción</option>
                                <option value="hombre">Hombre</option>
                                <option value="mujer">Mujer</option>
                            </select>
                        </div>
                    </div>
                </div>

                <div className="form-row">
                    <div className="input-group">
                        <label htmlFor="estadoCivil">Estado Civil</label>
                        <div className="input-wrapper no-icon">
                            <select id="estadoCivil" className="select-field">
                                <option value="">Seleccione una opción</option>
                                <option value="soltero">Soltero/a</option>
                                <option value="casado">Casado/a</option>
                                <option value="viudo">Viudo/a</option>
                                <option value="divorciado">Divorciado/a</option>
                            </select>
                        </div>
                    </div>
                    <div className="input-group">
                        <label htmlFor="movil">Teléfono Móvil</label>
                        <div className="input-wrapper">
                            <i className="input-icon-font">📱</i>
                            <input type="tel" id="movil" placeholder="600 000 000" />
                        </div>
                    </div>
                </div>

                <div className="form-row full-width">
                    <div className="input-group">
                        <label htmlFor="email">Correo Electrónico</label>
                        <div className="input-wrapper">
                            <i className="input-icon-font">✉️</i>
                            <input type="email" id="email" placeholder="ejemplo@correo.com" />
                        </div>
                    </div>
                </div>

                <div className="form-footer">
                    <button type="button" className="btn-cancel-link">Cancelar</button>
                    <button type="button" className="btn-next-action">
                        Siguiente <span>→</span>
                    </button>
                </div>
            </div>
        </main>
    );
};

export default AltaHermano;