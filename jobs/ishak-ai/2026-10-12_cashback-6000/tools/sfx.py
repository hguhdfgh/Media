import numpy as np, wave, sys
SR=48000; DUR=28.9; out=np.zeros(int(SR*DUR)); rng=np.random.default_rng(7)
def add(sig,t,g=1.0):
    i=int(t*SR); n=min(len(sig),len(out)-i); out[i:i+n]+=sig[:n]*g
def env(n,a,d): 
    e=np.ones(n); A=int(a*SR); e[:A]=np.linspace(0,1,max(A,1)); e[A:]=np.exp(-np.linspace(0,d,n-A)); return e
def lp(x,k):  # one-pole lowpass, k in (0,1)
    y=np.zeros_like(x); s=0
    for i in range(len(x)): s+=k*(x[i]-s); y[i]=s
    return y
def whoosh(d=.45,up=True):
    n=int(d*SR); x=rng.standard_normal(n); t=np.linspace(0,1,n)
    k=(.02+.25*t) if up else (.27-.25*t)
    y=np.zeros(n); s=0
    for i in range(n): s+=k[i]*(x[i]-s); y[i]=s
    return y*np.sin(np.pi*t)**1.5*2.2
def impact(d=.7):
    n=int(d*SR); t=np.arange(n)/SR; f=55+90*np.exp(-t*25)
    body=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*6)
    click=lp(rng.standard_normal(n),.3)*np.exp(-t*40)*.6
    return (body+click)*.9
def tick(f=2600): n=int(.03*SR); t=np.arange(n)/SR; return np.sin(2*np.pi*f*t)*np.exp(-t*160)*.35
def pop(f=880):
    n=int(.18*SR); t=np.arange(n)/SR; ff=f*(1+.6*np.exp(-t*60))
    return np.sin(2*np.pi*np.cumsum(ff)/SR)*np.exp(-t*22)*.5
def ding(f=1320):
    n=int(1.0*SR); t=np.arange(n)/SR
    return (np.sin(2*np.pi*f*t)+.5*np.sin(2*np.pi*f*2.01*t)+.25*np.sin(2*np.pi*f*3.02*t))*np.exp(-t*5)*.28
def shimmer(d=1.2):
    n=int(d*SR); t=np.arange(n)/SR; y=np.zeros(n)
    for f in (1760,2217,2637,3520): y+=np.sin(2*np.pi*f*t+rng.random()*6)
    return y*np.sin(np.pi*np.minimum(t/d,1))*.07*np.exp(-t*1.2)
def riser(d=.6):
    n=int(d*SR); t=np.arange(n)/SR; f=200+1400*(t/d)**2
    return np.sin(2*np.pi*np.cumsum(f)/SR)*(t/d)**2*.15 + whoosh(d)*.4
# timeline
add(impact(),0.0,.8); add(whoosh(.35,False),0.0,.5)
for x in np.arange(.14,1.04,.055): add(tick(2400+800*x),x,.8)
add(impact(),1.06,1.0); add(ding(),1.08,.8)
add(pop(1100),2.4,.8)
add(whoosh(.4),3.2,.7)
add(whoosh(.4),3.95,.8); add(pop(1500),4.42,.6)
for a in (5.44,6.44,7.74): add(pop(990),a,.8)
add(ding(1568),7.76,.6)
add(riser(.5),7.9,.8); add(whoosh(.5),8.25,1.0); add(impact(.5),8.4,.6)
for a,b in ((8.74,9.3),(9.6,10.2),(10.44,11.2),(11.48,12.1),(12.6,13.75),(13.98,15.0)):
    for x in np.arange(a,b,.06): add(tick(2200 if a in (8.74,10.44,12.6) else 3000),x,.6)
for a in (9.6,11.48): add(ding(1320),a+.5,.6)
add(impact(),14.9,1.0); add(ding(1760),14.92,.8); add(shimmer(),14.95,1.0)
add(whoosh(.45,False),15.2,.9)
add(whoosh(.5),15.95,.9); add(pop(700),16.5,.6)
add(riser(.9),18.25,.6); add(ding(1980),19.3,.5)
add(whoosh(.4),19.65,.7); add(pop(1100),20.3,.8)
add(whoosh(.4),21.3,.7); add(impact(.5),21.5,.5); add(shimmer(1.0),21.7,1.0)
for x in np.arange(23.1,23.65,.05): add(tick(2800),x,.6)
add(ding(1568),23.65,.6)
add(impact(),24.14,.9); add(impact(),24.84,1.1)
add(whoosh(.5),25.15,1.0); add(shimmer(1.6),25.35,1.4); add(impact(.6),25.3,.5)
add(pop(1200),26.3,.8); add(pop(1500),26.6,.7)
out=out/np.max(np.abs(out))*.9
w=wave.open(sys.argv[1],'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
