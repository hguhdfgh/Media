import sys,glob,os,numpy as np
from PIL import Image
from scipy import ndimage
src,dst=sys.argv[1],sys.argv[2]
names={'01':'headset','02':'card_plain','03':'loop','04':'burst','05':'phone','06':'briefcase','07':'coin','08':'calendar',
       '09':'plane','12':'shield','13':'stack','14':'stopwatch','15':'tiktok','16':'visa'}
for f in sorted(glob.glob(src+'/*.jpg')):
    k=os.path.basename(f)[:2]
    if k not in names: continue
    a=np.asarray(Image.open(f).convert('RGB')).astype(np.float32)
    R,G,B=a[...,0],a[...,1],a[...,2]
    m=np.minimum(R,B)-G                      # magenta-ness
    alpha=1-np.clip((m-40)/(150-40),0,1)
    # keep only bg connected to border as transparent; interior pink reflections stay opaque-ish
    bgmask=m>90
    lab,_=ndimage.label(bgmask); border=set(np.unique(np.r_[lab[0],lab[-1],lab[:,0],lab[:,-1]]))-{0}
    conn=np.isin(lab,list(border))
    conn=ndimage.binary_dilation(conn,iterations=2)
    alpha=np.where(conn,alpha,np.maximum(alpha,0.0) if False else np.clip(alpha+0.6,0,1))
    alpha=ndimage.gaussian_filter(alpha,0.7)
    # despill
    ex=np.clip(np.minimum(R,B)-G,0,None)
    R2=R-ex; B2=B-ex
    out=np.dstack([R2,G,B2,alpha*255]).clip(0,255).astype(np.uint8)
    im=Image.fromarray(out,'RGBA')
    bb=Image.fromarray((alpha>0.05).astype(np.uint8)*255).getbbox()
    im=im.crop(bb)
    im.save(f"{dst}/{names[k]}.png",optimize=True)
    print(names[k],im.size)
