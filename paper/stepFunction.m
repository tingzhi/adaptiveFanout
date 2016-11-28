clear all
clc
x = 0:0.2:1;
y = 1:1:5;
y(end+1) = 5;
stairs(x,y,'LineWidth',2, 'Color', 'k')

%plot(t,y)

axis([0, 1 0 5.5])

title('Adaptive Fanout Function')
xlabel('Remaining Energy Fraction')
ylabel('Fanout')