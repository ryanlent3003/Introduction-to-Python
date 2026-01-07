#create a two row vertical barplot figure with no margin between subplots
fig, ax = plt.subplots(nrows=2, ncols=1)
#set vspace to zero
fig.subplots_adjust(hspace=0)

ax[0].bar(animals, friendliness, 
          color='grey',
          edgecolor='black' #black edge around bars
          )
ax[0].set_ylabel("Friendliness")

#have the spines in ax[0] at the 0 on the y-axis
ax[0].spines['bottom'].set_position(('data', 0))

#set the tickmarks for the y-axis be in incremeents of 1
ax[0].yaxis.set(ticks=range(-3, 5, 1))

ax[1].bar(animals, popularity,
          color='grey',
          edgecolor='black' #black edge around bars
          )
ax[1].set_ylabel("Popularity")
plt.show()
