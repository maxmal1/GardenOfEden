# GardenOfEden

A Flask web app where users can create and manage their own plots at locations they choose. Additionally, users can add plants to these plots, indicating what they've planted. Users can create an account, or log on. Users who do not wish to create an account can still view publicly posted plots. This app used sql-alchemy for database implementation.

Needs a google maps API key to work.

All users can view any added plots.
![All users can view any added plots.](https://github.com/maxmal1/GardenOfEden/blob/main/project/static/opening_plots.png)
Users may sign up to add plots or add plants. This sign up uses flask-login for security.
![Users may sign up to add plots or add plants. This sign up uses flask-login for security.](https://github.com/maxmal1/GardenOfEden/blob/main/project/static/sign_up.png)
Once a user has logged in, they may edit their listed plots.
![Once a user has logged in, they may edit their listed plots.](https://github.com/maxmal1/GardenOfEden/blob/main/project/static/plots.png)
Users may add any plant, but can only remove plants that they've listed. 
![Users may add any plant, but can only remove plants that they've listed. ](https://github.com/maxmal1/GardenOfEden/blob/main/project/static/add_plant.png)


