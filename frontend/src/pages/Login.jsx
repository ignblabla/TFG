import Form from "../components/Form";
import Navbar from "../components/NavBar";

function Login() {
    return (
        <div className="site-wrapper">
            <Navbar />

            <Form route="/api/token/" method="login" />
        </div>
    );
}

export default Login;