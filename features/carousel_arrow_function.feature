Feature: Banner Carousel Navigation

    @case6
    Scenario: User navigates through the banner carousel
        Given the user is on the homepage for carousel arrow function
        When the user clicks the right arrow on the banner carousel
        And the user clicks the right arrow again
        Then the new banner should be loaded
        When the user clicks the left arrow on the banner carousel
        Then the previous banner should be displayed
