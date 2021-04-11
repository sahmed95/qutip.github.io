a = destroy(10); H = a.dag() * a ; c_ops = [np.sqrt(0.5) * a, np.sqrt(0.25) * a.dag()]
psi0 = rand_ket(10)
times = np.linspace(0, 100, 100)
medata = mesolve(H, psi0, times, c_ops, [a.dag() * a, a + a.dag(), -1j * (a - a.dag())])
np.shape(medata.expect)
# (3, 100)
times.shape
# (100,)
output_data = np.vstack((times, medata.expect))   # join time and expt data
file_data_store('expect.dat', output_data.T) # Note the .T for transpose!
with open("expect.dat", "r") as f:
   print('\n'.join(f.readlines()[:10]))
# # Generated by QuTiP: 100x4 complex matrix in decimal format [',' separated values].
# 0.0000000000+0.0000000000j,3.2109553666+0.0000000000j,0.3689771549+0.0000000000j,0.0185002867+0.0000000000j
# 1.0101010101+0.0000000000j,2.6754598872+0.0000000000j,0.1298251132+0.0000000000j,-0.3303672956+0.0000000000j
# 2.0202020202+0.0000000000j,2.2743186810+0.0000000000j,-0.2106241300+0.0000000000j,-0.2623894277+0.0000000000j
# 3.0303030303+0.0000000000j,1.9726633457+0.0000000000j,-0.3037311621+0.0000000000j,0.0397330921+0.0000000000j
# 4.0404040404+0.0000000000j,1.7435892209+0.0000000000j,-0.1126550232+0.0000000000j,0.2497182058+0.0000000000j
# 5.0505050505+0.0000000000j,1.5687324121+0.0000000000j,0.1351622725+0.0000000000j,0.2018398581+0.0000000000j
# 6.0606060606+0.0000000000j,1.4348632045+0.0000000000j,0.2143080535+0.0000000000j,-0.0067820038+0.0000000000j
# 7.0707070707+0.0000000000j,1.3321818015+0.0000000000j,0.0950352763+0.0000000000j,-0.1630920429+0.0000000000j
# 8.0808080808+0.0000000000j,1.2533244850+0.0000000000j,-0.0771210981+0.0000000000j,-0.1468923919+0.0000000000j
