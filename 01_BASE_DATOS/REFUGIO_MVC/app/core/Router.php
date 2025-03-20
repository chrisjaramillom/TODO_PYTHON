<?php
class Router
{
    public function run()
    {
        $url = isset($_GET['url']) ? rtrim($_GET['url'], '/') : 'home/index';
        $url = explode('/', $url);

        $controllerName = !empty($url[0]) ? ucfirst($url[0]) . 'Controller' : 'HomeController';
        $methodName = isset($url[1]) ? $url[1] : 'index';
        $param = isset($url[2]) ? $url[2] : null;

        $controllerFile = "../app/controllers/" . $controllerName . ".php";

        if (file_exists($controllerFile)) {
            require_once $controllerFile;
            $controller = new $controllerName();

            if (method_exists($controller, $methodName)) {
                if ($param) {
                    $controller->$methodName($param);
                } else {
                    $controller->$methodName();
                }
            } else {
                echo "❌ Error 404: Método '$methodName' no encontrado.";
            }
        } else {
            echo "❌ Error 404: Controlador '$controllerName' no encontrado.";
        }
    }
}
