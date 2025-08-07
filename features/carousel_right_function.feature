Feature: Extended Banner Carousel Interaction

    @case5
    Scenario: User navigates through multiple banners using carousel arrows
        Given the user is viewing the homepage banner section
        When the initial banner should be visible
        When the user taps the right navigation arrow once
        And the banner should update to the next item
        When the user taps the right navigation arrow again
        And the banner should refresh with a new image
        When the user continues by clicking the right arrow two more times
        And the final banner in the sequence should be displayed
        Then the previous banner should reappear
