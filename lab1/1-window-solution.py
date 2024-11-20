import pygame


def main():
    # init pygame modules
    pygame.init()
    title = "2DT904 - Setting the stage"
    screenSize = [512, 512]
    displayFlags = pygame.DOUBLEBUF | pygame.OPENGL

    # use a core ogl profile for cross-platform compatibility
    pygame.display.gl_set_attribute(
        pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

    # create and display the window
    pygame.display.set_mode(screenSize, displayFlags)
    pygame.display.set_caption(title)
    
    
    

    pygame.display.flip()

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


main()
