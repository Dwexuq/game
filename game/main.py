import glfw
from OpenGL.GL import *

def main():
    # GLFW penceresini başlat
    glfw.init()
    glfwWindowHint(GLFW_DECORATED, GLFW_FALSE);
    window = glfw.create_window(1360, 768, "", None, None)
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        # Oyun döngüsü
        glClear(GL_COLOR_BUFFER_BIT)

        # Oyun mantığı ve grafik çizimi buraya gelecek

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()