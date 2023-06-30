clc
clear all

%% Input Data
M_1 = readmatrix('result_Sony_small_L1\log_loss.txt');
M_2 = readmatrix('result_Sony_small_L2\log_loss.txt');
% M_SSIM = readmatrix('result_Sony_small_SSIM\log_loss.txt');


%% Plotting 
close all

figure(1)
plot(M_1)
title('Loss - Our Default Pipeline')
grid on
xlabel('Iteration')
xlim([0 2000])
ylabel('Magnitude')

figure(2)
plot(M_2)
title('Loss - L1 \rightarrow L2')
grid on
xlabel('Iteration')
xlim([0 2000])
ylabel('Magnitude')

% figure(3)
% plot(M_SSIM)
% title('Loss - L1 \rightarrow SSIM')
% grid on
% xlabel('Iteration')
% xlim([0 2000])
% ylabel('Magnitude')
