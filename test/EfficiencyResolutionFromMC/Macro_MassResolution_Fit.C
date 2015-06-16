#include "TProfile.h"
#include "TProfile.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH3F.h"
#include "TF1.h"
#include "TF2.h"
#include <string>
using std::string;
void Macro_MassResolution_Fit(){
    gROOT->Reset();
    gROOT->SetStyle("Plain");
    gStyle->SetStatFormat("5.3f");
    gStyle->SetFitFormat("5.3f");
    //gStyle->SetStatFormat("5.3f");
    //gStyle->SetFitFormat("5.3f");
    //int BoxValue = 6611; //4680;
    //int BoxValue = 11111111; //4680;
    int BoxValue = 6601; //4680;
    gStyle->SetOptFit(11);
    gStyle->SetOptDate(0);
    gStyle->SetOptTitle(0);
    gStyle->SetOptStat(BoxValue);
    //gStyle->SetOptStat(kFALSE);
    gStyle->SetPadBorderMode(0);
    gStyle->SetCanvasColor(0); //(10);
    gStyle->SetPadLeftMargin(0.15);
    gStyle->SetPadBottomMargin(0.15);
    gStyle->SetPalette(0);
    TPaveLabel pl;
    TLatex lt;
    //lt.SetTextFont(62);
    lt.SetTextFont(70);
    lt.SetTextAlign(12);
    lt.SetTextSize(0.07);
    lt.SetTextColor(1);
    int NbBins   = 10;
    float MinBin = -1.0;
    float MaxBin =  1.0;
    int NbBinsTheta   = 100;
    float MinBinTheta =  -1000.0;  //0.0;
    float MaxBinTheta =  1000.0;  //180.0;
    float FitMin      = -0.1; //-0.07;
    float FitMax      = 0.1; //0.07;
    //float FitMin      = -0.2;
    //float FitMax      = 0.2;
    float norm = 1.0;
    //==================================================================
    //==================================================================
    //==================================================================
    //==================================================================
    
    TCanvas *c8 = new TCanvas("c8","relative mass resolution",500,500);
    gPad->SetTopMargin(0.12);
    gPad->SetLeftMargin(0.15);
    gPad->SetFillColor(0);
    gPad->SetTickx();
    gPad->SetTicky();
    gPad->SetGridy();
    gPad->SetGridx();
    const Int_t n = 5;
    Float_t x[n]  = {140.0, 250.0, 1580.0, 3640.0, 6030.0};
    Float_t y[n]  = {0.0154,0.02,0.0432,0.0535,0.07};
    Float_t ex[n] = {0.0,0.0,0.0,0.0,0.0};
    Float_t ey[n] = {0.00023,0.00024,0.0005,0.0008,0.00178};
    TGraphErrors *gr = new TGraphErrors(n,x,y,ex,ey);
    gr->SetTitle("relative mass resolution");
    gr->GetXaxis()->SetTitle("dilepton mass (GeV)");
    gr->GetYaxis()->SetTitle("dilepton relative mass resolution");
    gr->GetXaxis()->SetTitleOffset(1.3);
    gr->GetYaxis()->SetTitleOffset(1.7);
    gr->SetLineStyle(0);
    gr->SetLineColor(1);
    gr->SetLineWidth(2);
    gr->SetMarkerColor(1);
    gr->SetMarkerStyle(20);
    gr->SetMarkerSize(0.875);
    gr->Draw("AP");
    gr->GetYaxis()->SetRangeUser(0.01,0.1);
    TF1* fn1 = new TF1("fn1",FittingFunc1,120,6000.0,3);
    //fn1->SetParameters(4.64567e-03,-1.75397e+02,-3.02480e-01);
    fn1->SetLineColor(2);
    //gr->Fit("fn1","R");
    //+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    TPaveText* tText1 = new TPaveText(0.20, 0.70, 0.50, 0.87, "brNDC");
    tText1->SetBorderSize(0);
    tText1->SetFillColor(0);
    tText1->SetFillStyle(0);
    TText *t1 = tText1->AddText("CMS, MC, #sqrt{s} = 13 TeV");
    TText *t2 = tText1->AddText("CMSSW720");
    TText *t3 = tText1->AddText("Phys14");
    Float_t tsize1 = 0.035;
    tText1->SetTextSize(tsize1);
   // tText1->Draw();
    //+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    TPaveText* tText2 = new TPaveText(0.40, 0.10, 0.70, 0.30, "brNDC");
    tText2->SetBorderSize(0);
    tText2->SetFillColor(0);
    tText2->SetFillStyle(0);
    TText *t1 = tText2->AddText("#sigma(m)/m=0.005/(m-175.395)^{-0.302}");
    Float_t tsize2 = 0.04;
    tText2->SetTextSize(tsize2);
    //tText2->Draw();
    //==========================================================
    TLegend *leg = new TLegend(0.30, 0.50, 0.50, 0.70);
    leg->AddEntry(gr,"Tune P Best Muon Track","p");
    leg->SetBorderSize(0.0);
    leg->SetMargin(0.3);
    leg->SetFillColor(0);
    leg->SetFillStyle(10);
    leg->SetLineColor(0);
    Float_t tsize2 = 0.03;
    leg->SetTextSize(tsize2);
    //leg->Draw();
    //=======================================================================
    c8->Print("MC-Zprime5000-CMSSW720-MassResolution-fit_All_points.png","png");
    //c8->Print("PlotsDir/MC-DY400-MLP-Eta1-CMSSW532-500-E25-2000-EE.eps","eps");
    //=======================================================================
    
    
}
///////////////// Fit with 9 parameters function ////////////
Double_t FittingFunc5(Double_t *x,Double_t *par)
{
    double xx = x[0];
    Double_t function= par[0]*(par[1]+ par[2]*pow(cos(xx),2));
    
    //Double_t function= par[0]*(1+par[1]*x[0]+par[2]*pow(x[0],2)+par[3]*pow(x[0],3)+par[4]*pow(x[0],4))*(1+par[5]*x[1]+par[6]*pow(x[1],2)+par[7]*pow(x[1],3)+par[8]*pow(x[1],4));
    
    
    
    return function;
}


Double_t FittingFunc1(Double_t *x,Double_t *par)
{
    double y = x[0];
    //Double_t function= par[0]/pow((y+par[1]),par[2]);
    Double_t function= par[0]+ y*par[1]+ y*y*par[2];
    return function;
}


Double_t FittingFunc2(Double_t *x,Double_t *par)
{
    double M = x[0];
    Double_t function= par[0]+par[1]/(M*M+par[2]);
    //Double_t function= par[0]+par[1]/pow(y+par[2],par[3]);
    return function;
}





Double_t FittingFunc3(Double_t *x,Double_t *par)
{
    double xx = x[0];
    Double_t function= par[0]/ pow((pow(xx,2) - par[1]*xx + par[2]),par[3]);
    return function;
}

Double_t FittingFunc4(Double_t *x,Double_t *par)
{
    double xx = x[0];
    Double_t function= exp( par[0] + par[1]*xx);
    
    //Double_t function= par[0]*(1+par[1]*x[0]+par[2]*pow(x[0],2)+par[3]*pow(x[0],3)+par[4]*pow(x[0],4))*(1+par[5]*x[1]+par[6]*pow(x[1],2)+par[7]*pow(x[1],3)+par[8]*pow(x[1],4));
    
    
    
    return function;
}





