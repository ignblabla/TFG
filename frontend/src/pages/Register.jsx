import Form from "../components/Form"
import Navbar from "../components/NavBar"

function Register() {
    return (
        <div className="site-wrapper">
            <Navbar />

            <Form route="/api/user/register/" method="register" />
        </div>
    )
}

export default Register