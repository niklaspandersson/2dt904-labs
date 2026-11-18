import pygame


def main():
    # init pygame modules
    pygame.init()

    # use a core ogl profile for cross-platform compatibility
    pygame.display.gl_set_attribute(
        pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

    # create and display the window
    pygame.display.set_mode(
        [512, 512], pygame.DOUBLEBUF | pygame.OPENGL, vsync=1)
    pygame.display.set_caption("2DT904 - Setting the stage")

    running = True
    while running:
        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


main()
